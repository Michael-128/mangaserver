async function search(keyword) {

    const url = 'https://graphql.anilist.co'

    const query = `
    query ($title: String) {
        Media(search: $title, type: MANGA) {
            title {
                native
            }
            staff {
                edges {
                    id
                    role
                    node {
                        name {
                            native
                            full
                        }
                    }
                }
            }
            description
            volumes
            chapters
        }
    }
    `

    const variables = {
        title: keyword
    }

    return await fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify({
            query: query,
            variables: variables
        })
    })
        .then(res => {
            if(res.ok)
                return res.json()
        })
        .then(json => {
            const media = json.data.Media

            const title = media.title.native

            try {
                const authors = Array.from(media.staff.edges.filter(edge => {
                    return edge.role.toLowerCase().includes("story") || edge.role.toLowerCase().includes("art")
                })).flatMap(staff => {
                    let name = staff.node.name
                    if(name.native != null) return name.native
                    return name.full
                })

               var author = authors.join(", ")
            } catch {
                console.warn("Author not found.")
            }
            console.log(media)
            return {
                title,
                author,
                description: media.description,
                volume_total: media.volumes,
                chapter_total: media.chapters
            }
        })
}


(function() {
    const mangaNameField = $("#id_name")
    
    if(!mangaNameField) {
        console.error("Name field not found.")
        return
    }

    let mangaNameFieldRow = mangaNameField.parent().parent();
    const mangaNameFieldParent = document.createElement("td")
    mangaNameFieldRow.append(mangaNameFieldParent)

    console.log(mangaNameFieldParent, mangaNameField)

    const searchButton = document.createElement("button")
    searchButton.className = "button is-primary"
    searchButton.innerText = "Search"
    searchButton.class = "button"

    $(searchButton).on("click", (e) => {
        e.preventDefault()

        if(mangaNameField.val().length < 1) return

        search(mangaNameField.val()).then(media => {
            console.log(media)
            $("#id_name").val(media.title)
            $("#id_author").val(media.author)
            $("#id_description").val(media.description)
            $("#id_volume_total").val(media.volume_total)
            $("#id_chapter_total").val(media.chapter_total)
        })
    })

    mangaNameFieldParent.append(searchButton)
    $("#search_btn").addClass("button")
})()



